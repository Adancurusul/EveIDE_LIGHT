
reg                  a_clk;
reg                  a_rst_n;
reg                  a_winc;
reg    [DSIZE-1:0]   a_wdata;
reg                  a_rinc;
wire   [DSIZE-1:0]   a_rdata;
wire                 a_full;
wire                 a_afull;
wire                 a_empty;
wire                 a_aempty;
reg                  a_dir;
reg                  b_clk;
reg                  b_rst_n;
reg                  b_winc;
reg    [DSIZE-1:0]   b_wdata;
reg                  b_rinc;
wire   [DSIZE-1:0]   b_rdata;
wire                 b_full;
wire                 b_afull;
wire                 b_empty;
wire                 b_aempty;
reg                  b_dir;

async_bidir_fifo#(
    .DSIZE      (8     ),
    .ASIZE      (4     ),
    .FALLTHROUGH("TRUE")
) inst_async_bidir_fifo(
    .a_clk         (),
    .a_rst_n       (),
    .a_winc        (),
    .a_wdata       (),
    .a_rinc        (),
    .a_rdata       (),
    .a_full        (),
    .a_afull       (),
    .a_empty       (),
    .a_aempty      (),
    .a_dir         (),
    .b_clk         (),
    .b_rst_n       (),
    .b_winc        (),
    .b_wdata       (),
    .b_rinc        (),
    .b_rdata       (),
    .b_full        (),
    .b_afull       (),
    .b_empty       (),
    .b_aempty      (),
    .b_dir         ()
);