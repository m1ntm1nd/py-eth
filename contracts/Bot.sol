pragma solidity ^0.8.10;

import "@openzeppelin/contracts/access/Ownable.sol";

contract Bot is Ownable{

    enum Actions {
        TRADE,
        CHECK
    }

    address private target;
}