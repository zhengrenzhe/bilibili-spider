<template>
    <card column="4">
        <card-title>Queue</card-title>
        <table v-if="queues.length !== 0" cellspacing="0">
            <thead>
            <tr>
                <td>Name</td>
                <td>State</td>
                <td>Consumers</td>
                <td>Ready</td>
                <td>Unacked</td>
                <td>Incoming Rate</td>
                <td>Ack Rate</td>
                <td>Priority Lengths</td>
            </tr>
            </thead>
            <tbody>
            <tr v-for="q in queues" :key="q.name">
                <td>{{q.name}}</td>
                <td><i class="state-indicate"></i>{{q.state}}</td>
                <td>{{q["consumers"]}}</td>
                <td>{{q["messages_ready"]}}</td>
                <td>{{q["messages_unacknowledged"]}}</td>
                <td>{{q["message_stats"]["publish_details"]["rate"]}}/s</td>
                <td>{{q["message_stats"]["ack_details"]["rate"]}}/s</td>
                <td class="priority-block">
                    <div v-for="(p, l, i) in q['backing_queue_status']['priority_lengths']" :key="i">
                        <div v-if="p !== 0" class="priority">
                            <div class="label">{{l}}</div>
                            <div class="count">{{p}}</div>
                        </div>
                    </div>
                </td>
            </tr>
            <tr></tr>
            </tbody>
        </table>
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
        data() {
            return {
                queues: [],
            };
        },
        created() {
            setInterval(() => {
                axios.get(`${API_BASE}/queue_info`).then(({data}) => {
                    this.queues = data.items;
                });
            }, 1000);
        },
    };
</script>

<style scoped lang="scss">
    table {
        width: 100%;
    }

    thead tr {
        color: #9FA9BA;

        td {
            padding: 8px 10px;
        }
    }

    tbody tr {
        color: #494b4c;

        td {
            padding: 8px 10px;
            font-weight: 600;
        }

        &:nth-child(2n+1) {
            background: #F8FAFC;
        }
    }

    .state-indicate {
        width: 10px;
        height: 10px;
        border-radius: 100%;
        background-color: #2ecc71;
        display: inline-block;
        margin-right: 6px;
        vertical-align: middle;
    }

    .priority {
        position: relative;
        display: inline-block;
        background-color: #e74c3c;
        color: #fff;
        border-radius: 4px;
        padding: 3px;
        font-size: 14px;
        margin-right: 14px;

        .label {
            position: absolute;
            font-size: 12px;
            left: -8px;
            top: -5px;
            background-color: #e74c3c;
            border-radius: 100%;
            width: 16px;
            height: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
        }

        .count {
            padding: 0 4px;
        }
    }

    .priority-block {
        display: flex;
    }
</style>