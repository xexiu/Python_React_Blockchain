import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import { API_BASE_URL } from '../constants/api';
import { TransactionProps } from '../types/transaction';
import Transaction from './Transaction';

const FIVE_SECONDS = 5000;

interface NetworkErrorInterface {
    error?: string;
}

function TransactionPool() {
    const navigate = useNavigate();
    const [transactions, setTransactions]: [TransactionProps[], Dispatch<SetStateAction<TransactionProps[]>>] = useState<TransactionProps[]>([]);
    // tslint:disable-next-line: max-line-length
    const [networkError, setNetworkError]: [NetworkErrorInterface, Dispatch<SetStateAction<NetworkErrorInterface>>] = useState<NetworkErrorInterface>({});

    async function fetchTransactions() {
        try {
            const res = await fetch(`${API_BASE_URL}/transactions`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            });
            const transactions = await res.json();
            return setTransactions(transactions);
        } catch (err: any) {
            if (err.message === 'Failed to fetch') {
                setNetworkError({
                    'error': `Error: ${err.messageServer}! Server is not started. Please start the server by running: python -m backend.app`
                });
            }
        }
    }

    async function fetchMineBlock() {
        try {
            const res = await fetch(`${API_BASE_URL}/blockchain/mine`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            });

            return navigate('/blockchain');

        } catch (err: any) {
            if (err.message === 'Failed to fetch') {
                setNetworkError({
                    'error': `Error: ${err.messageServer}! Server is not started. Please start the server by running: python -m backend.app`
                });
            }
        }
    }

    useEffect(() => {
        fetchTransactions();

        const intervalId = setInterval(fetchTransactions, FIVE_SECONDS);

        return () => {
            return clearInterval(intervalId);
        };
    }, []);

    const { error } = networkError as NetworkErrorInterface;

    return (
        <div className='TransactionPool'>
            <Link to='/'>Home</Link>
            <br />
            <h3>Transaction Pool</h3>
            <hr />
            <div>
                {
                    transactions.map((transaction: TransactionProps): JSX.Element => {
                        return (
                            <div key={transaction.id}>
                                <Transaction transaction={transaction} />
                            </div>
                        );
                    })
                }
            </div>
            <hr />
            <div>
                <Button variant='danger' onClick={fetchMineBlock}>
                    Mine a block
                </Button>
            </div>
            {error && <div>{error}</div>}
        </div>
    );
}

export default TransactionPool;
