module tb_gpr;

reg clk;
reg rst;
reg [7:0] register_write;
reg rd_r0_mux;
reg rd_r1_mux;
reg [2:0] ds1_rx;
reg [2:0] ds2_rx;
reg [7:0] rd_data;
reg [15:0] cr_data;
wire [7:0] ds1_data;
wire [7:0] ds2_data;
wire [15:0] r6_r7_data;

initial begin
    $from_myhdl(
        clk,
        rst,
        register_write,
        rd_r0_mux,
        rd_r1_mux,
        ds1_rx,
        ds2_rx,
        rd_data,
        cr_data
    );
    $to_myhdl(
        ds1_data,
        ds2_data,
        r6_r7_data
    );
end

gpr dut(
    clk,
    rst,
    register_write,
    rd_r0_mux,
    rd_r1_mux,
    ds1_rx,
    ds2_rx,
    rd_data,
    cr_data,
    ds1_data,
    ds2_data,
    r6_r7_data
);

endmodule
