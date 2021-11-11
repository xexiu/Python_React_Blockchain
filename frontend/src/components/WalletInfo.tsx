import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { API_BASE_URL } from '../constants/api';
import { WalletProps } from '../types/wallet';

function WalletInfo(): JSX.Element {
    const [walletInfo, setWalletInfo]: [WalletProps | {}, Dispatch<SetStateAction<object>>] = useState({});

    useEffect(() => {
        fetch(`${API_BASE_URL}/wallet/info`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        })
            .then(res => res.json())
            .then((wallet: WalletProps) => setWalletInfo(wallet))
            .catch(err => {
                if (err.message === 'Failed to fetch') {
                    setWalletInfo({
                        'error': `Error: ${err.messageServer}! Server is not started. Please start the server by running: python -m backend.app`
                    });
                }
            });
        return () => { };
    }, []);

    const { address, balance, error } = walletInfo as WalletProps;

    return (
        <div className='walletInfo'>
            <div>Address: {address}</div>
            <div>Balance: {balance}</div>
            {error && <div>{error}</div>}
        </div>
    );
}

export default WalletInfo;
