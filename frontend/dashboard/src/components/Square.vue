<template>
    <div class="square">
        <slot></slot>
    </div>
</template>

<script>
    export default {
        name: "Square",
    };
</script>

<style scoped lang="scss">
    .square {
        position: relative;

        &:before {
            content: "";
            padding-top: 100%;
            display: block;
        }
    }
</style>