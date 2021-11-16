import { Dispatch, SetStateAction, useCallback, useEffect, useState } from 'react';
import { API_BASE_URL, DEFAULT_FECTH_GET_PARAMS, DEFAULT_FETCH_POST_PARAMS } from '../constants/api';

interface ValuesInterface {
    data?: string[];
    error?: string;
    isLoading?: boolean;
}

function useFetch(url: string = '') {
    const [allValues, setAllValues]: [ValuesInterface, Dispatch<SetStateAction<ValuesInterface>>] = useState<ValuesInterface>({
        data: [],
        error: '',
        isLoading: true
    });

    const post = useCallback(async (_url: string = '', params = { ...DEFAULT_FETCH_POST_PARAMS }) => {
        const mergedParams = {
            ...DEFAULT_FETCH_POST_PARAMS,
            ...params
        };

        try {
            const res = await fetch(`${API_BASE_URL}${_url}`, mergedParams);
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

    const get = useCallback(async (_url: string = '', params = DEFAULT_FECTH_GET_PARAMS) => {
        const mergedParams = {
            ...DEFAULT_FECTH_GET_PARAMS,
            ...params
        };
        try {
            const res = await fetch(`${API_BASE_URL}${_url}`, mergedParams);
            const data = await res.json();
            if (url !== _url) {
                return data;
            }
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
    }, [url]);

    useEffect(() => {
        get(url);
        return () => { };
    }, [get, url]);

    const { data = [], isLoading = true, error = '' } = allValues;

    return { isLoading, data, error, post, get };
}

export {
    useFetch
};
