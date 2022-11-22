const app = Vue.createApp({
    delimiters: ["{", "}"],
    data() {
        return {
            username: 'Sidekick - Fast API Example',
            tasks: null,
            taskValue: ''
        }
    },
    mounted() { // le composant est monte
        axios.get('/api/tasks')
        .then((response) => {
            // On recupere les data dans notre taskList
            this.tasks = response.data
        })
    },
    methods: {
        addTask() {
            const newTask = {
                content: this.taskValue
            }

            // On envoie une requete post pour la sauvegarder ...
            axios.post('/api/create-task/', newTask)
            .then(response => {
                this.tasks = [...this.tasks, response.data]
            })

            this.taskValue = ''
        } 
    }
})