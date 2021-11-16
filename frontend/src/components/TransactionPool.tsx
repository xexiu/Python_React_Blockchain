import { useCallback, useEffect } from 'react';
import { Button } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import { useFetch } from '../custom-hooks/useFetch';
import Transaction from './Transaction';

const FIVE_SECONDS = 5000;

function TransactionPool() {
    const navigate = useNavigate();
    const { isLoading, data: transactions, error, get } = useFetch('/transactions');

    async function fetchMineBlock() {
        await get('/blockchain/mine');

        return navigate('/blockchain');
    }

    const fetchTransactions = useCallback(async () => {
        return await get('/transactions');
    }, [get]);

    useEffect(() => {
        fetchTransactions();

        const intervalId = setInterval(fetchTransactions, FIVE_SECONDS);

        return () => {
            return clearInterval(intervalId);
        };
    }, [fetchTransactions]);

    return (
        <div className='TransactionPool'>
            <Link to='/'>Home</Link>
            <br />
            <h3>Transaction Pool</h3>
            <hr />
            <div>
                {
                    transactions?.length && transactions.map((transaction: any): JSX.Element => {
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
            {isLoading && <p>Loading...</p>}
            {error && <div>{error}</div>}
        </div>
    );
}

export default TransactionPool;
