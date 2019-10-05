<template>
    <card column="4">
        <card-title>
            Count
            <div class="count">
                Total: {{count}} videos
            </div>
            <div class="ctrl">
                <button @click="changeTime('5d')" :disabled="current === '5d'">5 days</button>
                <button @click="changeTime('1h')" :disabled="current === '1h'">1 hour</button>
                <button @click="changeTime('5m')" :disabled="current === '5m'">5 minutes</button>
            </div>
        </card-title>
        <iframe :src="currentUrl"></iframe>
    </card>
</template>

<script>
    import Card from "./Card";
    import CardTitle from "./CardTitle";

    const urlMap = {
        "5d": "http://172.21.0.10:5601/app/kibana#/visualize/edit/ce8d16d0-e46a-11e9-92d5-6d199b200d7d?embed=true&_g=(refreshInterval%3A(pause%3A!t%2Cvalue%3A0)%2Ctime%3A(from%3Anow-5d%2Cto%3Anow))",
        "1h": "http://172.21.0.10:5601/app/kibana#/visualize/edit/ce8d16d0-e46a-11e9-92d5-6d199b200d7d?embed=true&_g=(refreshInterval%3A(pause%3A!t%2Cvalue%3A0)%2Ctime%3A(from%3Anow-1h%2Cto%3Anow))",
        "5m": "http://172.21.0.10:5601/app/kibana#/visualize/edit/ce8d16d0-e46a-11e9-92d5-6d199b200d7d?embed=true&_g=(refreshInterval%3A(pause%3A!t%2Cvalue%3A0)%2Ctime%3A(from%3Anow-5m%2Cto%3Anow))",
    };

    export default {
        name: "Count",
        components: {
            Card,
            CardTitle,
        },
        data() {
            return {
                current: "5d",
                currentUrl: urlMap["5d"],
            };
        },
        computed: {
            count() {
                return this.$store.state.video_count;
            },
        },
        methods: {
            changeTime(newTime) {
                this.current = newTime;
                this.currentUrl = urlMap[newTime];
            },
        },
    };
</script>

<style scoped lang="scss">
    .count {
        margin-left: 10px;
        font-size: 20px;
    }

    iframe {
        border: none;
        width: 100%;
        height: 300px;
    }

    .ctrl {
        display: flex;
        margin-left: auto;

        button {
            margin-left: 10px;
            cursor: pointer;
        }
    }
</style>