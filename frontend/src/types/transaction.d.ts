export type TransactionInputObj = {
    timestamp: number;
    amount: number;
    address: string;
    public_key: string;
    signature: string;
}

export type TransactionOutputObj = {
    timestamp: number;
    amount: number;
    address: string;
    public_key: string;
    signature: string;
}

export type TransactionProps = {
    id: string;
    input: TransactionInputObj;
    output: any;
};
