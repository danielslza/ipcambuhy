<template>
  <q-page class="q-pa-md bg-grey-2">

    <!-- Header -->
    <div class="row items-center justify-between q-mb-lg">
      <div>
        <h5 class="q-my-none text-primary text-weight-bold">Gestão de Membros</h5>
        <div class="text-caption text-secondary">Administração Interna - IPB</div>
      </div>

      <q-btn
        color="primary"
        icon="person_add"
        label="Cadastrar Membro"
        unelevated
        @click="abrirFormulario()"
      />
    </div>

    <!-- Lista -->
    <q-list bordered separator class="bg-white rounded-borders shadow-2">

      <q-item v-if="membros.length === 0" class="q-pa-xl text-center">
        <q-item-section class="text-grey-6">
          Nenhum membro cadastrado ou erro ao carregar dados.
        </q-item-section>
      </q-item>

      <q-item v-for="membro in membros" :key="membro.id" class="q-py-md">

        <q-item-section avatar>
          <q-avatar color="primary" text-color="white" icon="person" />
        </q-item-section>

        <q-item-section>
          <q-item-label class="text-weight-bold">
            {{ membro.nome }}
          </q-item-label>

          <q-item-label caption class="row q-gutter-x-md">
            <span>
              <q-icon name="phone" size="14px" />
              {{ membro.telefone || 'Sem tel.' }}
            </span>

            <span>
              <q-icon name="email" size="14px" />
              {{ membro.email || 'Sem e-mail' }}
            </span>
          </q-item-label>

          <q-item-label v-if="membro.is_lideranca">
            <q-badge color="primary" label="Liderança" outline />
          </q-item-label>
        </q-item-section>

        <q-item-section side>
          <div class="row q-gutter-xs">
            <q-btn flat round color="secondary" icon="edit" @click="abrirFormulario(membro)">
              <q-tooltip>Editar</q-tooltip>
            </q-btn>

            <q-btn flat round color="negative" icon="delete" @click="excluirMembro(membro.id)">
              <q-tooltip>Excluir</q-tooltip>
            </q-btn>
          </div>
        </q-item-section>

      </q-item>
    </q-list>

    <!-- Modal -->
    <q-dialog v-model="modalAberto" persistent>
      <q-card style="min-width: 400px" class="q-pa-sm">

        <q-card-section class="row items-center justify-between">
          <div class="text-h6 text-primary">
            {{ editando ? 'Editar Membro' : 'Novo Cadastro' }}
          </div>

          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section>

          <q-form @submit="salvarMembro" class="q-gutter-md">

            <q-input
              v-model="form.nome"
              label="Nome Completo *"
              filled
              :rules="[val => !!val || 'Nome é obrigatório']"
            />

            <q-input v-model="form.email" label="E-mail" type="email" filled />

            <q-input
              v-model="form.telefone"
              label="Telefone"
              filled
              mask="(##) #####-####"
              unmasked-value
            />

            <q-input
              v-model="form.data_nascimento"
              label="Data de Nascimento"
              filled
              mask="####-##-##"
            >
              <template #append>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                    <q-date v-model="form.data_nascimento" mask="YYYY-MM-DD">
                      <div class="row justify-end">
                        <q-btn v-close-popup label="Ok" color="primary" flat />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>

            <q-toggle
              v-model="form.is_lideranca"
              label="Este membro faz parte da liderança?"
              color="primary"
            />

            <div class="row justify-end q-mt-md">
              <q-btn label="Cancelar" color="secondary" flat v-close-popup />
              <q-btn
                :label="editando ? 'Atualizar' : 'Salvar'"
                type="submit"
                color="primary"
                unelevated
                class="q-ml-sm"
              />
            </div>

          </q-form>

        </q-card-section>
      </q-card>
    </q-dialog>

  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { api } from 'src/boot/axios'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// State

const membros = ref([])
const modalAberto = ref(false)
const editando = ref(false)

const formInicial = {
  id: null,
  nome: '',
  email: '',
  telefone: '',
  data_nascimento: '',
  is_lideranca: false
}

const form = ref({ ...formInicial })


// Helpers

const resetForm = () => {
  form.value = { ...formInicial }
}

// API

const carregarMembros = async () => {
  try {
    const { data } = await api.get('/membros')
    membros.value = data
  } catch (err) {
    console.error(err)
    $q.notify({
      color: 'negative',
      message: 'Erro ao conectar com o servidor'
    })
  }
}

const salvarMembro = async () => {
  try {
    const payload = form.value

    if (editando.value) {
      await api.patch(`/membros/${payload.id}`, payload)
      $q.notify({ color: 'positive', message: 'Membro atualizado!' })
    } else {
      await api.post('/membros', payload)
      $q.notify({ color: 'positive', message: 'Membro cadastrado!' })
    }

    modalAberto.value = false
    resetForm()
    carregarMembros()

  } catch (err) {
    console.error(err)
    $q.notify({ color: 'negative', message: 'Erro ao salvar dados' })
  }
}

const excluirMembro = (id) => {
  $q.dialog({
    title: 'Confirmar Exclusão',
    message: 'Tem certeza que deseja remover este membro?',
    cancel: true,
    persistent: true
  }).onOk(async () => {
    try {
      await api.delete(`/membros/${id}`)
      $q.notify({ color: 'warning', message: 'Membro removido' })
      carregarMembros()
    } catch (err) {
      console.error(err)
      $q.notify({ color: 'negative', message: 'Erro ao excluir' })
    }
  })
}

// UI

const abrirFormulario = (membro = null) => {
  if (membro) {
    form.value = { ...membro }
    editando.value = true
  } else {
    resetForm()
    editando.value = false
  }

  modalAberto.value = true
}

onMounted(carregarMembros)
</script>