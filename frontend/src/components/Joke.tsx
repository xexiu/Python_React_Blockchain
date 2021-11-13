import { Dispatch, SetStateAction, useEffect, useState } from 'react';
import { API_BASE_URL } from '../constants/api';
import { JokeProps } from '../types/jokes';

interface JokeInterface extends JokeProps {
    error?: string;
}

function Joke(): JSX.Element {
    const [joke, setJoke]: [JokeInterface, Dispatch<SetStateAction<object>>] = useState({});

    useEffect(() => {
        fetch(`${API_BASE_URL}/jokes/random_joke`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        })
            .then(res => res.json())
            .then((joke: JokeInterface) => setJoke(joke))
            .catch(err => {
                if (err.message === 'Failed to fetch') {
                    setJoke({
                        'error': `Error: ${err.messageServer}! Server is not started. Please start the server by running: python -m backend.app`
                    });
                }
            });
        return () => {

        };
    }, []);

    const { error } = joke as JokeInterface;

    function getFirstJoke() {
        const { setup, punchline } = joke as JokeInterface;
        return (
            <div>
                <p>{setup}</p>
                <p>{punchline}</p>
            </div>
        );
    }

    return (
        <div>
            {
                getFirstJoke()
            }
            {error && <div>{error}</div>}
        </div>
    );
}

export default Joke;
