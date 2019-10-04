<template>
    <div class="card" :style="styleObj">
        <slot></slot>
    </div>
</template>

<script>
    export default {
        name: "Card",
        data() {
            return {
                styleObj: {
                    "grid-column": `span ${this.column}`,
                },
            };
        },
        props: {
            column: {
                type: String,
                required: false,
                default: "1",
            },
        },
    };
</script>

<style scoped>
    .card {
        background-color: #fff;
        padding: 10px;
        border-radius: 4px;
        box-shadow: 0 0 10px 0 #e4e4e4;
    }
</style>