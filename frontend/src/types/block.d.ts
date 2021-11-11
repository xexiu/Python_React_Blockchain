import { TransactionProps } from '../types/transaction';

export type BlockProps = {
    data: TransactionProps[];
    difficulty: number;
    hash: string;
    last_hash: string;
    nonce: string;
    timestamp: number;
};
