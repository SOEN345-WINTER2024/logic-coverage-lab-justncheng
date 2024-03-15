import org.junit.Assert;
import org.junit.Test;

public class CheckItTest {

    @Test
    public void testTrueWithATrue() {
        // Test where condition should be true because a is true
        Assert.assertEquals("P is true", CheckIt.checkIt(true, false, false));
    }

    @Test
    public void testTrueWithBandCTrue() {
        // Test where condition should be true because both b and c are true
        Assert.assertEquals("P is true", CheckIt.checkIt(false, true, true));
    }

    @Test
    public void testFalseWithBFalse() {
        // Test where condition should be false because b is false (and a is false)
        Assert.assertEquals("P isn't true", CheckIt.checkIt(false, false, true));
    }

    @Test
    public void testFalseWithCFalse() {
        // Test where condition should be false because c is false (and a is false)
        Assert.assertEquals("P isn't true", CheckIt.checkIt(false, true, false));
    }
}
