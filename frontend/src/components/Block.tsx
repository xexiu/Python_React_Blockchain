import { useState } from 'react';
import { Button } from 'react-bootstrap';
import { MILI_SECONDS_PY } from '../constants/time';
import { BlockProps } from '../types/block';
import { TransactionProps } from '../types/transaction';
import Transaction from './Transaction';

function ToggleTransaction({ block }: BlockProps | any) {
    const [displayTransaction, setDisplayTransaction] = useState(false);
    const { data } = block as BlockProps;

    const toggleDisplay = () => setDisplayTransaction(!displayTransaction);

    if (displayTransaction) {
        return (
            <div>
                {
                    data.map((transaction: TransactionProps) => {
                        return (
                            <div key={transaction.id}>
                                <hr />
                                <Transaction transaction={transaction} />
                            </div>
                        );
                    })
                }
                <br />
                <Button variant='danger' size='sm' onClick={toggleDisplay}>
                    Show Less
                </Button>
            </div>
        );
    }

    if (data.length) {
        return (
            <Button variant='danger' size='sm' onClick={toggleDisplay}>
                Show More
            </Button>
        );
    }

    return null;
}

function Block({ block }: BlockProps | any): JSX.Element {
    const { timestamp, hash } = block as BlockProps;
    const hashDisplay = `${hash.substring(0, 15)}...`;
    const timeDisplay = new Date(timestamp / MILI_SECONDS_PY).toLocaleString();

    return (
        <div className='Block'>
            <div>HASH: {hashDisplay}</div>
            <div>TIME: {timeDisplay}</div>
            <br />
            <ToggleTransaction block={block} />
        </div>
    );
}

export default Block;
