import { route } from 'quasar/wrappers'
import { createRouter, createMemoryHistory, createWebHistory, createWebHashHistory } from 'vue-router'
import routes from './routes'

export default route(function (/* { store, ssrContext } */) {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : (process.env.VUE_ROUTER_MODE === 'history' ? createWebHistory : createWebHashHistory)

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,
    history: createHistory(process.env.VUE_ROUTER_MODE === 'history' ? process.env.VUE_ROUTER_BASE : '')
  })

  // --- AQUI ESTÁ A MÁGICA ---
  Router.beforeEach((to) => {
    const isAuthenticated = localStorage.getItem('token_ipb')

    // Se a rota for para a área /admin e não estiver logado
    if (to.path.startsWith('/admin') && !isAuthenticated) {
      return { name: 'login' }
    }
    
    // Se logar e tentar ir para /login, manda direto para o admin
    if (to.path === '/login' && isAuthenticated) {
      return { name: 'painel-admin' }
    }
  })
  

  return Router
})