import { Dispatch, SetStateAction, useState } from 'react';
import { Button, FormControl, FormGroup } from 'react-bootstrap';
import { Link, useNavigate } from 'react-router-dom';
import { useFetch } from '../custom-hooks/useFetch';


function ConductTransaction() {
    const navigate = useNavigate();
    const { isLoading, data: knownAddresses, error, post } = useFetch('/known-addresses');
    const [amount, setAmount]: [number, Dispatch<SetStateAction<number>>] = useState<number>(0);
    const [recipient, setRecipient]: [string, Dispatch<SetStateAction<string>>] = useState<string>('');

    function handleUpdateRecipient(event: { target: { value: SetStateAction<string>; }; }) {
        return setRecipient(event.target.value) as unknown as SetStateAction<string>;
    }

    function handleUpdateAmount(event: { target: { value: SetStateAction<number | string> }; }) {
        return setAmount(Number(event.target.value)) as unknown as SetStateAction<number>;
    }

    async function submitTransaction() {
        const response = await post('/wallet/transact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({ recipient, amount })
        });

        if (response && Object.keys(response).length) {
            return navigate('/transaction-pool');
        }

        return null;
    }

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
                    knownAddresses?.length && knownAddresses.map((knownAddress: string, index: number): JSX.Element => {
                        return (
                            <span key={knownAddress}><u>{knownAddress}</u>{index !== knownAddresses.length - 1 ? ' ,' : ''}</span>
                        );
                    })
                }
            </div>
            {isLoading && <p>Loading...</p>}
            {error && <div>{error}</div>}
        </div>
    );
}

export default ConductTransaction;
