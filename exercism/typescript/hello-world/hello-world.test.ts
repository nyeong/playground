import { assertEquals } from "https://deno.land/std@0.163.0/testing/asserts.ts";
import { hello } from "./hello-world.ts";

Deno.test('Hello World says hello world', () => {
  assertEquals(hello(), 'Hello, World!')
})
