import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import { API_BASE_URL } from '../constants/api';
import { PAGE_RANGE } from '../constants/app';
import { BlockProps } from '../types/block';
import Block from './Block';


function Blockchain(): JSX.Element {
    const [blockchain, setBlockchain] = useState([]);
    const [error, setError] = useState('');
    const [blockchainLength, setBlockchainLength]: [number, Dispatch<SetStateAction<number>>] = useState(0);

    async function myFetch({ uri, cb }: { uri: string; cb: Function; }): Promise<void> {
        try {
            const res = await fetch(uri, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            });
            const blockchain = await res.json();
            return cb(blockchain);
        } catch (err: any) {
            if (err.message === 'Failed to fetch') {
                setError(`Error: ${err.messageServer}! Server is not started. Please start the server by running: python -m backend.app`);
            }
        }
    }

    function fetchBlockchainPage({ start = 0, end = PAGE_RANGE }: { start: number, end: number }): any {
        return myFetch({ uri: `${API_BASE_URL}/blockchain/page?start=${start}&end=${end}`, cb: setBlockchain });
    }

    useEffect(() => {
        myFetch({ uri: `${API_BASE_URL}/blockchain`, cb: setBlockchain });
        myFetch({ uri: `${API_BASE_URL}/blockchain/length`, cb: setBlockchainLength });
        return () => { };
    }, []);

    const buttonNumbers = [] as number[];

    for (let i = 0; i < blockchainLength / PAGE_RANGE; i++) {
        const number = i;
        buttonNumbers.push(number);
    }

    return (
        <div className='Blockchain'>
            <h3>Blockchain</h3>
            <div>
                {blockchain.map((block: BlockProps) => <Block key={block.hash} block={block} />)}
            </div>
            <div>
                {
                    buttonNumbers.map((number: number) => {
                        const start = number * PAGE_RANGE;
                        const end = (number + 1) * PAGE_RANGE;

                        return (
                            <span key={number}>
                                <Button variant='danger' size='sm' onClick={() => fetchBlockchainPage({ start, end })}>
                                    {number + 1}
                                </Button>
                            </span>
                        );
                    })
                }
            </div>
            {error && <div>{error}</div>}
        </div>
    );
}

export default Blockchain;
