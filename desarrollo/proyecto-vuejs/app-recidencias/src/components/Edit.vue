<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
                <label for="propietario">propietario</label>
                <input
                    type="text"
                    class="form-control"
                    id="propietario"
                    v-model="departamento.propietario"
                    v-validate="'required'"
                    name="propietario"
                    placeholder="Ingrese propietario"
                    :class="{'is-invalid': errors.has('departamento.propietario') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>
            <div class="form-group">
                <label for="costo">Costo departamento</label>
                <input
                    type="text"
                    class="form-control"
                    id="costo"
                    v-model="departamento.costo"
                    v-validate="'required'"
                    name="costo"
                    placeholder="Ingrese el costo del departamento"
                    :class="{'is-invalid': errors.has('departamento.costo') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>
            <div class="form-group">
                <label for="numCuartos">Número de Cuartos</label>
                <input
                    type="text"
                    class="form-control"
                    id="numCuartos"
                    v-model="departamento.numCuartos"
                    v-validate="'required'"
                    name="numCuartos"
                    placeholder="Ingrese el número de cuartos"
                    :class="{'is-invalid': errors.has('departamento.numCuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>
            <div class="form-group">
                <label for="edificio">Edificio</label>
                <input
                    type="text"
                    class="form-control"
                    id="edificio"
                    v-model="departamento.edificio"
                    v-validate="'required'"
                    name="edificio"
                    placeholder="Seleccione el edificio"
                    :class="{'is-invalid': errors.has('departamento.edificio') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
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
                url: '',
            },
            submitted: false
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/departamento/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.departamento = response.data
            });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8000/api/departamento/${this.departamento.id}/`,
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
