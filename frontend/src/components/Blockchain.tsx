import { useCallback, useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { PAGE_RANGE } from '../constants/app';
import { useFetch } from '../custom-hooks/useFetch';
import Block from './Block';


function Blockchain(): JSX.Element {
    const { isLoading, error, get } = useFetch();
    const [blockchain, setBlockchain] = useState([]);
    const [blockchainLength, setBlockchainLength] = useState(0);

    async function fetchBlockchainPage({ start = 0, end = PAGE_RANGE }: { start: number, end: number }): Promise<void> {
        const data = await get(`/blockchain/page?start=${start}&end=${end}`);

        return setBlockchain(data);
    }

    const fetchBlockchain = useCallback(async () => {
        const data = await get('/blockchain');

        return setBlockchain(data);
    }, [get]);

    const fetchBlockchainLength = useCallback(async () => {
        const data = await get('/blockchain/length');

        return setBlockchainLength(data);
    }, [get]);

    useEffect(() => {
        fetchBlockchain();
        fetchBlockchainLength();
        return () => { };
    }, [fetchBlockchain, fetchBlockchainLength]);

    const buttonNumbers = [] as number[];

    for (let i = 0; i < blockchainLength / PAGE_RANGE; i++) {
        const number = i;
        buttonNumbers.push(number);
    }

    return (
        <div className='Blockchain'>
            <h3>Blockchain</h3>
            <h6>Number of blockchains: {blockchainLength}</h6>
            <br />
            <Link to='/'>Home</Link>
            <br />
            <div>
                {blockchain?.length && blockchain.map((block: any): JSX.Element => <Block key={block.hash} block={block} />)}
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
            {isLoading && <p>Loading...</p>}
            {error && <div>{error}</div>}
        </div>
    );
}

export default Blockchain;
