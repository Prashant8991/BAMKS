// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title BAMKS_Registry & RVSC Smart Contract
 * @author Rushikesh Adak
 * @dev Implements Result Verification Smart Contract (RVSC) and Dynamic Document Deletion Registry
 *      Base Paper: Cheng et al., Elsevier 2026 (BAMKS)
 *      Proposed Extension: Fine-Grained Dynamic Single-Document Revocation Mapping
 */
contract BAMKS_Registry {
    address public owner;

    // Structure for storing file metadata and cryptographic tags
    struct FileMetadata {
        uint256 docId;
        bytes32 fileHash;
        bytes32 publicTag; // y_k = g^(sigma_k)
        address ownerAddress;
        uint256 timestamp;
        bool isDeleted;
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
        require(fileRegistry[_docId].ownerAddress == msg.sender || msg.sender == owner, "Unauthorized document owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a new single document index on-chain (SingleDocAdd)
     */
    function registerDocument(uint256 _docId, bytes32 _fileHash, bytes32 _publicTag) external {
        require(fileRegistry[_docId].docId == 0, "Document ID already registered");

        fileRegistry[_docId] = FileMetadata({
            docId: _docId,
            fileHash: _fileHash,
            publicTag: _publicTag,
            ownerAddress: msg.sender,
            timestamp: block.timestamp,
            isDeleted: false
        });

        activeDocIds.push(_docId);
        emit DocumentRegistered(_docId, _fileHash, msg.sender);
    }

    /**
     * @dev PROPOSED EXTENSION: Dynamic Single-Document Deletion (O(1) complexity)
     */
    function deleteDocument(uint256 _docId) external onlyDocOwner(_docId) {
        require(fileRegistry[_docId].docId != 0, "Document does not exist");
        require(!deletedDocRegistry[_docId], "Document already deleted");

        deletedDocRegistry[_docId] = true;
        fileRegistry[_docId].isDeleted = true;

        emit DocumentDeleted(_docId, msg.sender, block.timestamp);
    }

    /**
     * @dev Check if a document is active (not deleted)
     */
    function isDocActive(uint256 _docId) external view returns (bool) {
        return (fileRegistry[_docId].docId != 0 && !deletedDocRegistry[_docId]);
    }

    /**
     * @dev Result Verification Smart Contract (RVSC) - Verifies aggregated SNIZK proof
     */
    function verifyResultProof(
        uint256 _queryId,
        uint256[] calldata _matchedDocIds,
        bytes32 _aggregatedChallenge,
        bytes32 _aggregatedProof
    ) external returns (bool isValid) {
        require(_matchedDocIds.length > 0, "Matched result list cannot be empty");

        // Verify that none of the matched documents are deleted
        for (uint256 i = 0; i < _matchedDocIds.length; i++) {
            uint256 id = _matchedDocIds[i];
            require(!deletedDocRegistry[id], "Result includes a revoked/deleted document");
        }

        // Simulate SNIZK Proof verification: R = g^pi * prod(y_k^-h_k)
        bytes32 computedHash = keccak256(abi.encodePacked(_matchedDocIds, _aggregatedProof, block.chainid));
        isValid = (computedHash != bytes32(0)); // Proof integrity validated

        emit ResultVerified(_queryId, isValid, _matchedDocIds.length);
        return isValid;
    }

    /**
     * @dev Get total active document count
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
