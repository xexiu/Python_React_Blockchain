import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { Button, FormControl, FormGroup } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import { API_BASE_URL } from '../constants/api';

interface NetworkErrorInterface {
    error?: string;
}

function ConductTransaction() {
    const navigate = useNavigate();
    const [amount, setAmount]: [number, Dispatch<SetStateAction<number>>] = useState<number>(0);
    const [recipient, setRecipient]: [string, Dispatch<SetStateAction<string>>] = useState<string>('');
    // tslint:disable-next-line: max-line-length
    const [networkError, setNetworkError]: [NetworkErrorInterface, Dispatch<SetStateAction<NetworkErrorInterface>>] = useState<NetworkErrorInterface>({});
    const [knownAddresses, setKnownAddresses]: [string[], Dispatch<SetStateAction<string[]>>] = useState<string[]>([]);

    useEffect(() => {
        fetch(`${API_BASE_URL}/known-addresses`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        })
            .then(res => res.json())
            .then((addresses: string[]) => setKnownAddresses(addresses))
            .catch(err => {
                if (err.message === 'Failed to fetch') {
                    setNetworkError({
                        'error': `Error: ${err.messageServer}! Server is not started. Please start the server by running: python -m backend.app`
                    });
                }
            });
        return () => { };
    }, []);

    function handleUpdateRecipient(event: { target: { value: SetStateAction<string>; }; }) {
        return setRecipient(event.target.value) as unknown as SetStateAction<string>;
    }

    function handleUpdateAmount(event: { target: { value: SetStateAction<number | string> }; }) {
        return setAmount(Number(event.target.value)) as unknown as SetStateAction<number>;
    }

    function submitTransaction() {
        fetch(`${API_BASE_URL}/wallet/transact`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({ recipient, amount })
        })
            .then(res => res.json())
            .then((json) => {
                // console.log('submitted transaction json', json);
                return navigate('/transaction-pool');
            })
            .catch(err => {
                if (err.message === 'Failed to fetch') {
                    return setNetworkError({
                        'error': `Error: ${err.messageServer}! Server is not started. Please start the server by running: python -m backend.app`
                    });
                }
            });
    }

    const { error } = networkError as NetworkErrorInterface;

    return (
        <div className='ConductTransaction'>
            <h3>Conduct Transaction</h3>
            <br />
            <Link to='/'>Home</Link>
            <br />
            <hr />
            <FormGroup>
                <FormControl type='text' placeholder='recipient' value={recipient} onChange={handleUpdateRecipient} />
            </FormGroup>

            <FormGroup>
                <FormControl type='number' placeholder='amount' value={amount} onChange={handleUpdateAmount} />
            </FormGroup>
            <div>
                <Button variant='danger' onClick={submitTransaction}>
                    Submit
                </Button>
            </div>
            <hr />
            <h4>Known Addresses</h4>
            <div>
                {
                    knownAddresses.map((knownAddress: string, index: number): JSX.Element => {
                        return (
                            <span key={knownAddress}><u>{knownAddress}</u>{index !== knownAddresses.length - 1 ? ' ,' : ''}</span>
                        );
                    })
                }
            </div>
            {error && <div>{error}</div>}
        </div>
    );
}

export default ConductTransaction;
