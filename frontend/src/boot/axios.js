import axios from 'axios'

// Aqui definimos a URL do seu Django
const api = axios.create({ baseURL: 'http://localhost:8000/api' })

export { api }