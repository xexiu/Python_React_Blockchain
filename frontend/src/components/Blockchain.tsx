import { useEffect, useState } from 'react';
import { API_BASE_URL } from '../constants/api';
import { BlockProps } from '../types/block';
import Block from './Block';

function Blockchain(): JSX.Element {
    const [blockchain, setBlockchain] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        fetch(`${API_BASE_URL}/blockchain`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        })
            .then(res => res.json())
            .then((blockchain: any) => setBlockchain(blockchain))
            .catch(err => {
                if (err.message === 'Failed to fetch') {
                    setError(`Error: ${err.messageServer}! Server is not started. Please start the server by running: python -m backend.app`);
                }
            });
        return () => { };
    }, []);

    return (
        <div className='Blockchain'>
            <h3>Blockchain</h3>
            <div>
                {blockchain.map((block: BlockProps) => <Block key={block.hash} block={block} />)}
            </div>
            {error && <div>{error}</div>}
        </div>
    );
}

export default Blockchain;
