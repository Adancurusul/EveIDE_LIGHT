module tb_top;

reg clk;
reg rst;
wire write;
wire read;
reg rdy;
wire [15:0] pc;
reg [15:0] ins;
wire [15:0] addr;
wire [7:0] wdata;
reg [7:0] rdata;
reg int0;
reg int1;
reg int2;
reg int3;

initial begin
    $from_myhdl(
        clk,
        rst,
        rdy,
        ins,
        rdata,
        int0,
        int1,
        int2,
        int3
    );
    $to_myhdl(
        write,
        read,
        pc,
        addr,
        wdata
    );
end

top dut(
    clk,
    rst,
    write,
    read,
    rdy,
    pc,
    ins,
    addr,
    wdata,
    rdata,
    int0,
    int1,
    int2,
    int3
);

endmodule
