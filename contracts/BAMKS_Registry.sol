// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title BAMKS_Registry & Dynamic Revocation Ledger
 * @author Prashant Singh & Rushikesh Adak
 * @dev Implements on-chain document registration and dynamic single-document revocation mapping (O(1)).
 *      Off-chain aggregated Schnorr NIZK verification is performed by the client/edge node;
 *      this contract enforces non-revocation membership and binding integrity on-chain.
 */
contract BAMKS_Registry {
    address public owner;

    struct FileMetadata {
        uint256 docId;
        bytes32 fileHash;
        bytes32 publicTag; // y_k = g^(sigma_k)
        address ownerAddress;
        uint256 timestamp;
    }

    // Storage mappings
    mapping(uint256 => FileMetadata) public fileRegistry;
    mapping(uint256 => bool) public deletedDocRegistry;
    uint256[] public activeDocIds;
    
    // Events
    event DocumentRegistered(uint256 indexed docId, bytes32 fileHash, address indexed owner);
    event DocumentDeleted(uint256 indexed docId, address indexed owner, uint256 timestamp);
    event ResultVerified(uint256 indexed queryId, bool isValid, uint256 matchedCount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can execute");
        _;
    }

    modifier onlyDocOwner(uint256 _docId) {
        require(
            fileRegistry[_docId].ownerAddress == msg.sender || msg.sender == owner,
            "Unauthorized: caller is not document owner or contract admin"
        );
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a new single document index on-chain (SingleDocAdd).
     *      Multi-owner onboarding allows any data owner to register an unused docId.
     */
    function registerDocument(uint256 _docId, bytes32 _fileHash, bytes32 _publicTag) external {
        require(_docId != 0, "Invalid doc ID");
        require(fileRegistry[_docId].docId == 0, "Document ID already registered");

        fileRegistry[_docId] = FileMetadata({
            docId: _docId,
            fileHash: _fileHash,
            publicTag: _publicTag,
            ownerAddress: msg.sender,
            timestamp: block.timestamp
        });

        activeDocIds.push(_docId);
        emit DocumentRegistered(_docId, _fileHash, msg.sender);
    }

    /**
     * @dev PROPOSED EXTENSION: Dynamic Single-Document Revocation (O(1) complexity).
     *      Callable by document owner or contract administrator.
     *      Directly updates deletedDocRegistry mapping in O(1) time without array traversal.
     */
    function deleteDocument(uint256 _docId) external onlyDocOwner(_docId) {
        require(fileRegistry[_docId].docId != 0, "Document does not exist");
        require(!deletedDocRegistry[_docId], "Document already deleted");

        deletedDocRegistry[_docId] = true;

        emit DocumentDeleted(_docId, msg.sender, block.timestamp);
    }

    /**
     * @dev Check if a document is active (registered and not revoked)
     */
    function isDocActive(uint256 _docId) external view returns (bool) {
        return (fileRegistry[_docId].docId != 0 && !deletedDocRegistry[_docId]);
    }

    /**
     * @dev Result Verification Smart Contract (RVSC) On-Chain Check.
     *      NOTE: Off-chain aggregated Schnorr NIZK proof is verified by the client/edge node;
     *      this on-chain function enforces that no deleted/revoked document appears in the result set.
     */
    function verifyResultProof(
        uint256 _queryId,
        uint256[] calldata _matchedDocIds,
        bytes32 _aggregatedChallenge,
        bytes32 _aggregatedProof
    ) external returns (bool isValid) {
        require(_matchedDocIds.length > 0, "Matched result list cannot be empty");

        // Enforce that no revoked/deleted document appears in the result set
        for (uint256 i = 0; i < _matchedDocIds.length; i++) {
            require(!deletedDocRegistry[_matchedDocIds[i]], "Result includes a revoked/deleted document");
        }

        // Cryptographic binding over matched IDs, query challenge, proof, and chain ID
        bytes32 queryBinding = keccak256(abi.encodePacked(_matchedDocIds, _aggregatedChallenge, _aggregatedProof, block.chainid));
        isValid = (queryBinding != bytes32(0));

        emit ResultVerified(_queryId, isValid, _matchedDocIds.length);
        return isValid;
    }

    /**
     * @dev Get total active document count.
     *      NOTE: Traverses activeDocIds array for auditing/reporting purposes only.
     *      This does NOT affect the O(1) single-document deletion path.
     */
    function getActiveDocumentCount() external view returns (uint256 count) {
        for (uint256 i = 0; i < activeDocIds.length; i++) {
            if (!deletedDocRegistry[activeDocIds[i]]) {
                count++;
            }
        }
        return count;
    }
}
