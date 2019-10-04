<template>
    <div class="card-title">
        <slot></slot>
    </div>
</template>

<script>
    export default {
        name: "CardTitle",
    };
</script>

<style scoped lang="scss">
    .card-title {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        font-size: 30px;
        color: #2c3e50;
        line-height: 1;
        margin-bottom: 10px;
    }
</style>