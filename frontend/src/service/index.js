import axios from 'axios';
import { useAuthStore } from '../stores/auth/index.js'

const api = axios.create({
    baseURL: 'http://localhost:8000/api/v0.1.0',
});


api.interceptors.request.use(
    (config) => {
        const useStore = useAuthStore();
        const token = useStore.accessToken || localStorage.getItem("access_token")
        if(token){
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => Promise.reject(error)
)


api.interceptors.response.use(
    (response) => response,
    async (error) => {
        const useStore = useAuthStore()

        // si 401 et possede refresh token
        if(error.response && error.response.status === 401){
            try {
                const refreshToken = localStorage.getItem("refresh_token")
                if(refreshToken){
                    // call api pour refresh
                    const refreshResponse = await axios.post("http://127.0.0.1:8000/api/v0.1.0/auth/refresh_token", {}, {headers: { Authorization: `Bearer ${refreshToken}`}})

                    const newAccessToken = refreshResponse.data.access_token

                    // maj store
                    useStore.accessToken = newAccessToken
                    localStorage.setItem("access_token", newAccessToken)

                    // refais la requete originale
                    error.config.headers.Authorization = `Bearer ${newAccessToken}`
                    return api.request(error.config)
                } 
            } catch (refreshError){
                useStore.logout()
            }
        } 

        return Promise.reject(error)
    }
)

export default api;