<template>
    <card column="4">
        <card-title>Queue</card-title>
    </card>
</template>

<script>
    import axios from "axios";

    import Card from "./Card";
    import CardTitle from "./CardTitle";
    import {API_BASE} from "../store";

    export default {
        name: "Queue",
        components: {
            Card, CardTitle,
        },
        created() {
            setInterval(() => {
                axios.get(`http://${API_BASE}/queue_info`).then((res) => {
                    console.log(res);
                });
            }, 1000);
        },
    };
</script>

<style scoped>

</style>