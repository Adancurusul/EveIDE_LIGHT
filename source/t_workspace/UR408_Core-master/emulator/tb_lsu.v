module tb_lsu;

reg [15:0] r6_r7_data;
reg [15:0] ds1_data;
reg mem_read;
reg mem_write;
wire mem_ok;
wire [7:0] lsu_out;
wire [15:0] addr;
wire [7:0] wdata;
reg rdata;
wire write;
wire read;
reg rdy;

initial begin
    $from_myhdl(
        r6_r7_data,
        ds1_data,
        mem_read,
        mem_write,
        rdata,
        rdy
    );
    $to_myhdl(
        mem_ok,
        lsu_out,
        addr,
        wdata,
        write,
        read
    );
end

lsu dut(
    r6_r7_data,
    ds1_data,
    mem_read,
    mem_write,
    mem_ok,
    lsu_out,
    addr,
    wdata,
    rdata,
    write,
    read,
    rdy
);

endmodule
