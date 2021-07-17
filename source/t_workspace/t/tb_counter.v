//`include "counter.v"
`timescale 1ns/1ps

module tb_counter;
reg clk;
reg rst_n;
wire [4:0]od;

counter counter
(
    .rst_n (rst_n),
    .clk (clk),
    .ocnt(od)
);

localparam CLK_PERIOD = 2;
always #(CLK_PERIOD/2) clk=~clk;

initial begin
    $dumpfile("tb.lxt");
    $dumpvars(0, counter);
end

initial begin
    #1 rst_n<=1'bx;clk<=1'bx;
    #(CLK_PERIOD*3) rst_n<=1;
    #(CLK_PERIOD*3) rst_n<=0;clk<=0;
    repeat(5) @(posedge clk);
    rst_n<=1;
    repeat(64) @(posedge clk);
    $dumpflush;
    $stop;
end

endmodule