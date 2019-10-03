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
        padding: 14px;
        user-select: none;
        box-shadow: 0 0 2px 0 rgb(195, 195, 195);
        background-color: #FCFCFD;

        a {
            color: #33373B;
            text-decoration: none;
            font-size: 18px;
            font-weight: 600;
        }
    }
</style>