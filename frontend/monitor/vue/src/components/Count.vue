<template>
    <div class="count">
        <div class="title">Videos {{count}}</div>
    </div>
</template>

<script>
    export default {
        name: "Count",
        computed: {
            count() {
                return this.$store.state.videos_count;
            },
        },
    };
</script>

<style scoped lang="scss">
    .count {
        margin: 40px 20px;
        box-shadow: 0 0 2px 0 #c3c3c3;
        background-color: #fff;
        border-radius: 4px;
        padding: 10px 16px;
    }

    .title {
        font-size: 18px;
    }
</style>