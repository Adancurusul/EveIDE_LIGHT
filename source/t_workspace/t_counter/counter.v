`timescale 1ns/1ps

module counter(
    input clk,
    input rst_n,
    output reg [4:0]ocnt
    d
);

always@(posedge clk or negedge rst_n)
if (!rst_n) begin
    ocnt <= 5'd0;
end
else ocnt <= ocnt + 5'd1;

endmodule