import { TransactionProps } from '../types/transaction';

type recipient = string;

function Transaction({ transaction }: TransactionProps | any): JSX.Element {
    const { input, output } = transaction as TransactionProps;
    const recipients = Object.keys(output) as recipient[];

    return (
        <div className='Transaction'>
            <div>From: {input.address}</div>
            {
                recipients.map((recipient: recipient) => {
                    return (
                        <div key={recipient}>
                            To: {recipient} | Sent: {output[recipient]}
                        </div>
                    );
                })
            }
        </div>
    );
}

export default Transaction;
