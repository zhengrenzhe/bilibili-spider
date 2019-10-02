<template>
    <div class="header">
        <a href="/">Bilibili Monitor</a>
    </div>
</template>

<script>
    export default {
        name: "Header",
    };
</script>

<style scoped lang="scss">
    .header {
        padding: 10px 14px;
        background-color: indianred;
        font-size: 16px;
        user-select: none;
        box-shadow: 1px 1px 4px 0 rgb(195, 195, 195);

        a {
            color: #fff;
            text-decoration: none;
        }
    }
</style>