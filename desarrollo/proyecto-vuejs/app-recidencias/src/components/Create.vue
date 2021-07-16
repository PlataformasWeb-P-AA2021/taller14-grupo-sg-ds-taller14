<template>
<div class="pt-5">
    <form @submit.prevent="create" method="post">
        <div class="form-group">
            <label for="propietario">Nombre del propietario</label>
            <input type="text" class="form-control" id="propietario" v-model="departamento.propietario" v-validate="'required'" name="propietario" placeholder="Ingrese nombre del propietario" :class="{'is-invalid': errors.has('departamento.propietario') && submitted}">
            <div class="invalid-feedback">
                Please provide a valid name.
            </div>
        </div>
        <div class="form-group">
            <label for="costo">Costo del departamento</label>
            <input type="text" class="form-control" id="costo" v-model="departamento.costo" v-validate="'required'" name="costo" placeholder="Ingrese el costo" :class="{'is-invalid': errors.has('departamento.costo') && submitted}">
            <div class="invalid-feedback">
                Please provide a valid name.
            </div>
        </div>
        <div class="form-group">
            <label for="numCuartos">Número de Cuartos</label>
            <input type="text" class="form-control" id="numCuartos" v-model="departamento.numCuartos" v-validate="'required'" name="numCuartos" placeholder="Ingrese el número de cuartos" :class="{'is-invalid': errors.has('departamento.numCuartos') && submitted}">
            <div class="invalid-feedback">
                Please provide a valid name.
            </div>
        </div>
        <div class="form-group">
            <label for="edificio">Edificio</label>
            <select class="form-control" v-model="departamento.edificio">
                <option v-for="e in edificiosList" :key="e.url" :value="e.url">{{ e.nombre }}</option>
            </select>
        </div>
        <br>
        <div>
            <br>
            <button type="submit" class="btn btn-primary">Crear</button>
        </div>
    </form>
</div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                propietario: '',
                costo: '',
                numCuartos: '',
                edifcio: '',
            },
            edificiosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getEdificiosList()
    },
    methods: {
        getEdificiosList() {
            axios
                .get('http://127.0.0.1:8000/api/edificio/')
                .then(response => {
                    this.edificiosList = response.data
                })
                .catch(error => {
                    console.log(error)
                })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                console.log(this.propietario)
                axios.post('http://127.0.0.1:8000/api/departamento/',
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>
