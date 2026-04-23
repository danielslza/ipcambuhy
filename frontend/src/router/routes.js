const routes = [
  // --- PARTE PÚBLICA (Usa o PublicLayout) ---
  {
    path: '/',
    component: () => import('layouts/PublicLayout.vue'),
    children: [
      {
        path: 'home',
        name: 'inicio',
        component: () => import('pages/PublicHome.vue')
      },
      {
        path: 'login',
        name: 'login',
        component: () => import('pages/LoginPage.vue')
      }
    ]
  },

  // --- PARTE ADMINISTRATIVA (Usa o MainLayout) ---
  {
    path: '/admin',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'painel-admin',
        component: () => import('pages/PainelAdminPage.vue')
      }
    ]
  },

  // Erro 404
  {
    path: '/:catchAll(.*)*',
    name: 'erro-404',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes