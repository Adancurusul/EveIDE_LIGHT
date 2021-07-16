module tb_single_port_ram;

reg clk;
reg we;
reg [15:0] addr;
reg [15:0] din;
wire [15:0] dout;

initial begin
    $from_myhdl(
        clk,
        we,
        addr,
        din
    );
    $to_myhdl(
        dout
    );
end

single_port_ram dut(
    clk,
    we,
    addr,
    din,
    dout
);

endmodule
