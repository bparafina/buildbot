import build
import builder
import buildrequest
import buildset
import master
import slave
import testresult

# styles.Versioned requires this, as it keys the version numbers on the fully
# qualified class name; see master/buildbot/test/regressions/test_unpickling.py
build.BuildStatus.__module__ = 'buildbot.status.builder'

# add all of these classes to builder; this is a form of late binding to allow
# circular module references among the status modules
builder.BuildSetStatus = buildset.BuildSetStatus
builder.TestResult = testresult.TestResult
builder.SlaveStatus = slave.SlaveStatus
builder.Status = master.Status
builder.BuildStatus = build.BuildStatus
builder.BuildRequestStatus = buildrequest.BuildRequestStatus
