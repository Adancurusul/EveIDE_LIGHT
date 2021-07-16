module tb_id;

reg [15:0] ins;
wire [3:0] alu_signal;
wire mem_read;
wire mem_write;
wire [7:0] register_write;
wire rd_r0_mux;
wire rd_r1_mux;
wire [2:0] ds1_rx;
wire [2:0] ds2_rx;
wire rd_mux0;
wire rd_mux1;
wire cr_write;
wire [2:0] selector;
wire [7:0] imm;
wire [15:0] branch_offset;
wire bra;
wire ret;
wire apc;
wire jmp;

initial begin
    $from_myhdl(
        ins
    );
    $to_myhdl(
        alu_signal,
        mem_read,
        mem_write,
        register_write,
        rd_r0_mux,
        rd_r1_mux,
        ds1_rx,
        ds2_rx,
        rd_mux0,
        rd_mux1,
        cr_write,
        selector,
        imm,
        branch_offset,
        bra,
        ret,
        apc,
        jmp
    );
end

id dut(
    ins,
    alu_signal,
    mem_read,
    mem_write,
    register_write,
    rd_r0_mux,
    rd_r1_mux,
    ds1_rx,
    ds2_rx,
    rd_mux0,
    rd_mux1,
    cr_write,
    selector,
    imm,
    branch_offset,
    bra,
    ret,
    apc,
    jmp
);

endmodule
