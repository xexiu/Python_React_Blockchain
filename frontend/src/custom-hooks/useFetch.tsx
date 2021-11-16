import { Dispatch, SetStateAction, useCallback, useEffect, useState } from 'react';
import { API_BASE_URL, DEFAULT_FECTH_PARAMS } from '../constants/api';

interface ValuesInterface {
    data?: string[];
    error?: string;
    isLoading?: boolean;
}

function useFetch(url: string = '', params = DEFAULT_FECTH_PARAMS) {
    const [allValues, setAllValues]: [ValuesInterface, Dispatch<SetStateAction<ValuesInterface>>] = useState<ValuesInterface>({
        data: [],
        error: '',
        isLoading: true
    });

    const post = useCallback(async(_url, params) => {
        try {
            const res = await fetch(`${API_BASE_URL}${_url}`, params);
            return await res.json();
        } catch (err: any) {
            if (err.message === 'Failed to fetch') {
                const { message } = err;

                return setAllValues(prev => {
                    return {
                        ...prev,
                        error: message,
                        isLoading: false
                    };
                });
            }
        }
    }, []);

    const fetchData = useCallback(async () => {
        try {
            const res = await fetch(`${API_BASE_URL}${url}`, params);
            const data = await res.json();
            return setAllValues(prev => {
                return {
                    ...prev,
                    data,
                    error: '',
                    isLoading: false
                };
            });
        } catch (err: any) {
            if (err.message === 'Failed to fetch') {
                const { message } = err;

                return setAllValues(prev => {
                    return {
                        ...prev,
                        error: message,
                        isLoading: false
                    };
                });
            }
        }
    }, [url, params]);

    useEffect(() => {
        fetchData();
        return () => { };
    }, [fetchData]);

    const { data, isLoading, error } = allValues;

    return { isLoading, data, error, post };
}

export {
    useFetch
};
