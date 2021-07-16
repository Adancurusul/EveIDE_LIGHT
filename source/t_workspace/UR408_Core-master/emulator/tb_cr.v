module tb_cr;

wire [15:0] pc_next;
reg [15:0] branch_offset;
reg [15:0] r6_r7_data;
wire [15:0] cr_data;
reg clk;
reg rst;
reg int0;
reg int1;
reg int2;
reg int3;
reg mem_read;
reg mem_write;
reg mem_ok;
reg branch;
reg [2:0] selector;
reg cr_write;
reg ret;
reg apc;
reg jmp;
reg bra;
wire main_state;

initial begin
    $from_myhdl(
        branch_offset,
        r6_r7_data,
        clk,
        rst,
        int0,
        int1,
        int2,
        int3,
        mem_read,
        mem_write,
        mem_ok,
        branch,
        selector,
        cr_write,
        ret,
        apc,
        jmp,
        bra
    );
    $to_myhdl(
        pc_next,
        cr_data,
        main_state
    );
end

cr dut(
    pc_next,
    branch_offset,
    r6_r7_data,
    cr_data,
    clk,
    rst,
    int0,
    int1,
    int2,
    int3,
    mem_read,
    mem_write,
    mem_ok,
    branch,
    selector,
    cr_write,
    ret,
    apc,
    jmp,
    bra,
    main_state
);

endmodule
