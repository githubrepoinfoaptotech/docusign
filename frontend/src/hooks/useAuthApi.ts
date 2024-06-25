// src/hooks/useAuthApi.ts
import { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../redux/store';
import Axios from '../configs/AxiosConfig';

const useAuthApi = () => {
  const token = useSelector((state: RootState) => state.auth.token);

  useEffect(() => {
    const requestInterceptor = Axios.interceptors.request.use((config) => {
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    });

    return () => {
      Axios.interceptors.request.eject(requestInterceptor);
    };
  }, [token]);

  return Axios;
};

export default useAuthApi;