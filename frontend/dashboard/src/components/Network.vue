<template>
    <card>
        <card-title>
            Network
            <div v-if="system" class="speed">
                <span class="up">
                    <font-awesome-icon icon="long-arrow-alt-up"/>
                    {{system["network"]["upload"]}} KB/s
                </span>
                <span class="down">
                    <font-awesome-icon icon="long-arrow-alt-down"/>
                    {{system["network"]["download"]}} KB/s
                </span>
            </div>
        </card-title>
        <square>
            <canvas id="network-chart"></canvas>
        </square>
    </card>
</template>

<script>
    import Card from "./Card.vue";
    import CardTitle from "./CardTitle";
    import Square from "./Square";

    const now = Date.now();

    const uploadTimeSeries = Array(60).fill(0).map((_, i) => ({
        y: null,
        t: new Date(now - (1000 * i)),
    }));

    const downloadTimeSeries = Array(60).fill(0).map((_, i) => ({
        y: null,
        t: new Date(now - (1000 * i)),
    }));

    function appendTimeSeries(arr, item) {
        const n = arr.slice(1);
        n.push(item);
        return n;
    }

    export default {
        name: "Network",
        components: {
            Card, CardTitle, Square,
        },
        computed: {
            system() {
                const d = this.$store.state.stat;
                return d ? d.system : null;
            },
        },
        data() {
            return {
                networkChart: {},
            };
        },
        mounted() {
            this.networkChart = new Chart(document.getElementById("network-chart").getContext("2d"), {
                type: "bar",
                data: {
                    datasets: [
                        {
                            borderColor: "#e74c3c",
                            data: uploadTimeSeries,
                            type: "line",
                            pointRadius: 0,
                            fill: false,
                            borderWidth: 2,
                        },
                        {
                            borderColor: "#2ecc71",
                            data: downloadTimeSeries,
                            type: "line",
                            pointRadius: 0,
                            fill: false,
                            borderWidth: 2,
                        },
                    ],
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    legend: {
                        display: false,
                    },
                    animation: {
                        duration: 0,
                    },
                    layout: {
                        padding: {
                            top: 2,
                            bottom: 2,
                        },
                    },
                    scales: {
                        xAxes: [{
                            display: false,
                            type: "time",
                            distribution: "series",
                            ticks: {
                                source: "data",
                                autoSkip: true,
                            },
                        }],
                        yAxes: [{
                            display: false,
                        }],
                    },
                },
            });
        },
        created() {
            this.$store.subscribe((_, state) => {
                if (!state.stat.system) {
                    return;
                }

                this.networkChart.data.datasets[0].data = appendTimeSeries(this.networkChart.data.datasets[0].data, {
                    y: state.stat.system["network"]["upload"],
                    t: new Date(),
                });
                this.networkChart.data.datasets[1].data = appendTimeSeries(this.networkChart.data.datasets[1].data, {
                    y: state.stat.system["network"]["download"],
                    t: new Date(),
                });

                this.networkChart.update();
            });
        },
    };
</script>

<style scoped lang="scss">
    .speed {
        margin-left: 10px;
        font-size: 14px;
        display: flex;

        .up {
            color: #e74c3c;
            margin-right: 10px;
        }

        .down {
            color: #2ecc71;
        }
    }

    #network-chart {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
    }
</style>