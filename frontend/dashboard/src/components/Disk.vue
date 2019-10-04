<template>
    <card>
        <card-title>Disk</card-title>
        <div>
            <div class="item" v-for="d in disk" :key="d['mount_point']">
                <div class="title">
                    {{d["device"]}}&nbsp;&nbsp;&nbsp;&nbsp;{{d["mount_point"]}}
                </div>
                <div class="total">
                    <div :style="{width: `${d.used / d.total * 100}%`}" class="percent"></div>
                </div>
            </div>
        </div>
    </card>
</template>

<script>
    import Card from "./Card";
    import CardTitle from "./CardTitle";

    export default {
        name: "Disk",
        components: {
            Card, CardTitle,
        },
        computed: {
            disk() {
                const d = this.$store.state.stat;
                if (!d || !d.system) return [];
                return d.system["disk"];
            },
        },
    };
</script>

<style scoped lang="scss">
    .item {
        margin-top: 8px;

        .title {
            font-size: 16px;
            font-weight: 500;
        }

        .total {
            height: 40px;
            margin-top: 4px;
            border-radius: 4px;
            background-color: #e4e4e4;

            .percent {
                height: 100%;
                border-radius: 4px;
            }
        }

        &:nth-child(1) {
            .title {
                color: #e84118;
            }

            .percent {
                background-color: #e84118;
            }
        }

        &:nth-child(2) {
            .title {
                color: #fbc531;
            }

            .percent {
                background-color: #fbc531;
            }
        }

        &:nth-child(3) {
            .title {
                color: #00a8ff;
            }

            .percent {
                background-color: #00a8ff;
            }
        }

        &:nth-child(4) {
            .title {
                color: #6D214F;
            }

            .percent {
                background-color: #6D214F;
            }
        }

        &:nth-child(5) {
            .title {
                color: #2ed573;
            }

            .percent {
                background-color: #2ed573;
            }
        }
    }
</style>