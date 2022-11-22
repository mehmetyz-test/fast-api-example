app.component('task-item', {
    data(){
        return {
            isCompleted: false
        }
    },
    props: {
        description: {
            type: String,
            required: true
        }
    },
    template:
    /*html*/
    `
    <div class="task" :class="{ closed: isCompleted }">
        <p class="task-content"> {{ description }} </p>
        <input type="checkbox" v-model="isCompleted">
    </div>
    `
})