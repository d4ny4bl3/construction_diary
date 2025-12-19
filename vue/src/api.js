import axios from 'axios'
import router from '@/router'

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

api.interceptors.response.use(
    response => response,
    error => {
      if (error.response && [401, 403].includes(error.response.status)) {
        console.warn("SESSION EXPIRED – redirecting to login")
        router.push({ name: 'Login' })
      }
      return Promise.reject(error)
    }
)

export default api
