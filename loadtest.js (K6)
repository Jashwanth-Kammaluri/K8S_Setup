import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  scenarios: {
    performance_test: {
      executor: 'constant-arrival-rate',
      rate: 5000, 
      timeUnit: '1s',
      duration: '30s',
      preAllocatedVUs: 1000,
      maxVUs: 2000,
    },
  },
};

export default function () {
  const res = http.get('http://172.17.26.241:30146/');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'body is correct': (r) => r.body.includes('Hello from K8s'),
  });
}
