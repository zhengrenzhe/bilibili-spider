<template>
    <card>
        <card-title>Memory</card-title>
        <div :class="`item ${m.type}`" v-for="m in memory" :key="m.name">
            <div class="title">{{m.name}}</div>
            <div class="total">
                <div :style="{width: m['percent']}" class="percent"></div>
            </div>
        </div>
    </card>
</template>

<script>
    import Card from "./Card.vue";
    import CardTitle from "./CardTitle";
    import {toGBSize} from "../utils";

    export default {
        name: "Memory",
        components: {
            Card, CardTitle,
        },
        computed: {
            memory() {
                const d = this.$store.state.stat;
                if (!d || !d.system) {
                    return [];
                }

                const {memory, swap} = d.system;

                return [
                    {
                        name: `Physical (${toGBSize(memory.used)}/${toGBSize(memory.total)})`,
                        type: "physical",
                        percent: `${memory.used / memory.total * 100}%`,
                    },
                    {
                        name: `Swap (${toGBSize(swap.used)}/${toGBSize(swap.total)})`,
                        type: "swap",
                        percent: `${((swap.used / swap.total) || 0) * 100}%`,
                    },
                ];
            },
        },
    };
</script>

<style scoped lang="scss">
    .item {
        margin-top: 20px;

        .title {
            font-size: 18px;
            font-weight: 500;
        }

        .total {
            height: 40px;
            margin-top: 8px;
            border-radius: 4px;
            background-color: #e4e4e4;

            .percent {
                height: 100%;
                border-radius: 4px;
                transition: width 0.2s;
            }
        }
    }

    .physical {
        color: #ff6384;

        .percent {
            background-color: #ff6384;
        }
    }

    .swap {
        color: #36a2eb;

        .percent {
            background-color: #36a2eb;
        }
    }
</style>