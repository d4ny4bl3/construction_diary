import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true
})

api.interceptors.request.use(config => {
    const token = document.cookie.match(/csrftoken=([^;]+)/)?.[1]
    if (token && ['post', 'put', 'patch', 'delete'].includes(config.method)) {
        config.headers['X-CSRFTOKEN'] = token
    }
    return config
})

export default api
